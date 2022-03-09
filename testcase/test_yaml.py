import json

import yaml


class TestXueQiu:

    def test_search(self):
        # with open("../page/main.yaml",encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
        #     for step in steps:
        #         print("***********")
        #         print(step["by"].text)
        #         print(type(step["by"]))
        #         print(step["locator"])
        #         print(type(step["locator"]))
        #         print(step["action"])
        self._params = {"name":"阿里巴巴-SW"}
        # print(self._params)
        path = "../page/abc.yaml"
        with open(path,encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        raw = json.dumps(steps)
        for key,value in self._params.items():
            # ${name} | name:123
            # print(item)
            raw.replace(f'${{{key}}}',value)
        print(raw)
        # steps = json.loads(raw)

        # _param = {'name':"12345"}
        # str = "*** ${name} lll${name}llllllllllll"
        # for key,value in _param.items():
        #     print(key,value)
        #     str = str.replace('${{{key}}}',value)
        # str = str.replace('${name}','12345')
        # print(str)
