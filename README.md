# ansible-role-aide [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-aide.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-aide)

CentOS 7 に aide を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名            |デフォルト値               |説明
------------------|---------------------------|------------------------------
aide_include_list |/etc/aide.conf$  CONTENT_EX|改ざん検知対象リスト
aide_exclude_list |/root/\.ansible.*</br>/var/log/aide.log|改ざん非検知リスト
