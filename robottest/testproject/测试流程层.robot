*** Settings ***
Library           Selenium2Library
Resource          测试数据.robot
Resource          测试元素层.robot

*** Keywords ***
测试流程
    [Arguments]    ${url}
    打开浏览器    ${url}
    @{t}    搜索内容
    : FOR    ${w}    IN    @{t}
    \    Log    ${w}
    \    输入关键字    ${w}
    \    点击搜索
    \    校验标题    ${w}
    \    截图
    关闭浏览器
