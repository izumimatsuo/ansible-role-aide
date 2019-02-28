# ansible-role-aide

CentOS 7 に aide を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名            |デフォルト値               |説明
------------------|---------------------------|------------------------------
aide_include_files|/etc/aide.conf$  CONTENT_EX|改ざん検知対象リスト
aide_exclude_files|/root/\.ansible.*</br>/var/log/aide.log|改ざん非検知リスト
