*** Settings ***
Library           Selenium2Library
Library           DatabaseLibrary
Library           random

*** Keywords ***
content
    ${title}    Get Value    id=kw
    log    ${title}

Ukey
    Open Browser    https://www.baidu.com    Chrome
    Set Browser Implicit Wait    30
    Maximize Browser Window

打开浏览器
    [Arguments]    ${url}
    Open Browser    ${url}    gc
    Set Browser Implicit Wait    30
    Maximize Browser Window

输入关键字
    [Arguments]    ${word}
    Input Text    css = #kw    ${word}

点击搜索
    Click Button    id=su

校验标题
    [Arguments]    ${word}
    sleep    5
    Wait Until Page Contains    ${word}
    ${title}    Get Title
    Should Contain    ${title}    ${word}

截图
    Set Screenshot Directory    E:/python/robottest/testproject/image
    Capture Page Screenshot

关闭浏览器
    Close Browser

连接数据库
    Connect To Database Using Custom Params    pymysql    host='localhost',port=3306,user='root',passwd='123456',db='test'

关闭数据库
    Disconnect From Database

数据库新增数据
    [Arguments]    ${a}    ${b}
    Execute Sql String    insert into hhh value(${a}, ${b})

查询所有数据
    @{a}    Description    select * from hhh

删除数据
    [Arguments]    ${a}
    Execute Sql String    DELETE FROM hhh WHERE dd=${a}
