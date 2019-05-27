import allure, pytest


class Test001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试步骤01")
    def test_001_1(self):
        with open("./imgage\\Snipaste.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)
        print("-->test_001_1")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试步骤02")
    def test_001_2(self):
        print("-->test_001_2")
        allure.attach("标题", "具体内容")  # 添加描述信息
        assert True
