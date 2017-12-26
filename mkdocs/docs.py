#!/usr/bin/env python3
import io
import re
import os
import sys
import glob
import shutil
import optparse
import pprint
import yaml
import json


class Tasks:
    def __init__(self, args):
        parser = optparse.OptionParser()
        parser.add_option("-t", dest="task",
                          help="specify the main task [%s]" % ', '.join(['build', 'serve']))
        parser.add_option("--ignore-dirs", dest="ignore_dirs", default=json.dumps([]),
                          help="specify the masks to be ignored for mkdocs")
        parser.add_option("--theme", dest="theme", default="mkdocs",
                          help="specify the name of mkdocs theme")
        parser.add_option("-V", "--verbose", dest="verbose", action="store_true", default=False,
                          help="enable the verbose mode")
        self._initial_args = args

        self._options, self._args = parser.parse_args(args)

        self._setup()

        assert self._options.task in ['build', 'serve']

        self.mkdocs()

    def _setup(self):
        self.mkdocs_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__)))
        self.project_root = os.path.abspath(
            os.path.join(self.mkdocs_root, '..'))

        self.ignore_dirs = [
            os.path.abspath(os.path.join(self.project_root, p))
            for p in json.loads(self._options.ignore_dirs)
        ]

    def _dirs(self, p):
        res = []
        cur_p = p
        while True:
            cur_p = os.path.split(cur_p)
            res.insert(0, cur_p[1])

            if cur_p[0] == '':
                break

            cur_p = cur_p[0]

        return res

    def _parse(self, md):
        with io.open(md, 'r') as f:
            s = f.readline()
            _title_re = re.compile(r'(#+)\s*(.*)\s*')

            mg = _title_re.match(s)

            if mg is not None:
                _header_level = len(mg[1])
                _title = mg[2]
            else:
                _header_level = None
                _title = None

            parts = self._dirs(os.path.relpath(
                md, os.path.join(self.mkdocs_root, 'docs')))
            dir_parts = parts[:-1]

            if parts[-1].lower() == 'intro.md' and len(dir_parts) > 0:
                title = dir_parts[-1].capitalize()
            elif _title is not None and _header_level == 1:
                title = _title
            elif len(dir_parts) > 0:
                title = os.path.splitext(
                    parts[-1])[0].replace('_', ' ').title()
            else:
                title = None

            return {
                'fname': parts[-1],
                'file': os.path.relpath(md, os.path.join(self.mkdocs_root, 'docs')),
                'title': title,
                'folders': dir_parts
            }

    def _hierarchy(self, entries):
        hierarchy = {}

        for e in entries:
            _prev = hierarchy
            for k in e['folders']:
                _prev[k] = _prev.get(k, {})
                _prev = _prev[k]
            _prev[e['fname']] = e
            _prev[e['fname']]['is_node'] = True

        return hierarchy

    def _config(self, hierarchy):
        _stack = [list(hierarchy.items())]
        _pos = [0]
        _data = [[]]

        while True:
            cur_stack = _stack[-1]
            cur_data = _data[-1]
            _pos[-1]

            if _pos[-1] == len(cur_stack):
                if len(_stack) > 1:
                    _data[-2].append({_stack[-2][_pos[-2] - 1]
                                      [0].title(): cur_data})

                    _pos.pop()
                    _stack.pop()
                    _data.pop()
                    continue
                else:
                    break

            entry = cur_stack[_pos[-1]]
            _pos[-1] += 1

            if entry[1].get('is_node', False):
                cur_data.append({entry[1]['title']: entry[1]['file']})
            elif len(entry[1]) > 0:
                _stack.append(list(entry[1].items()))
                _data.append([])
                _pos.append(0)
                continue

        return _data[0]

    def _generate(self):
        mkds = glob.glob(os.path.join(self.mkdocs_root, 'docs', '**', '*.md')) +\
            glob.glob(os.path.join(self.mkdocs_root, 'docs', '*.md'))
        entries = [self._parse(md) for md in mkds]
        hierarchy = self._hierarchy(entries)
        _config = {
            'site_name': 'R2 "Book"',
            'theme': self._options.theme,
            'pages': self._config(hierarchy)
        }

        if self._options.verbose:
            pprint.pprint([mkds, entries, hierarchy, _config])

        _yaml = \
            r"""site_name: {site_name}
theme: {theme}

pages:
{pages}""".format(
                site_name=_config['site_name'],
                theme=_config['theme'],
                pages=yaml.dump(_config['pages'], default_flow_style=False)
            )

        return _yaml

    def mkdocs(self):
        fs = [
            p for p in
            glob.glob(os.path.join(self.project_root, '*/')) +
            glob.glob(os.path.join(self.project_root, '*.md'))
            if not os.path.abspath(p) in
            [self.mkdocs_root] + self.ignore_dirs
        ]

        os.system(r"""
        cd {mkdocs_root};
        rm -fr docs site;
        mkdir -p docs;
        """.format(mkdocs_root=self.mkdocs_root))

        for f in fs:
            src = f
            dst = os.path.join(self.mkdocs_root, 'docs',
                               os.path.relpath(f, self.project_root))
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy(src, dst)

        with io.open(os.path.join(self.mkdocs_root, 'mkdocs.yml'), 'w') as f:
            f.write(u'' + self._generate())

        os.system(r"""
        cd {mkdocs_root};
        {python} -m mkdocs {task};
        """.format(
            python=sys.executable,
            mkdocs_root=self.mkdocs_root,
            task=self._options.task)
        )


if __name__ == '__main__':
    Tasks(sys.argv[1:])
