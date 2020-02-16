*** Settings ***
Library           Selenium2Library

*** Keywords ***
linktest

跳转
    [Arguments]    ${text}
    Click Element    ${text}
