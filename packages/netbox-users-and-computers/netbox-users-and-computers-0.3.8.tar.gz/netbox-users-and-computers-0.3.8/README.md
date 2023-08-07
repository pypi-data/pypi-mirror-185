# Netbox plugin 'Users and Computers'

���������:
- � Netbox ������ "ADUsers"
- � Netbox ������ "Workstations"
- � �������� �������� virtual machine, device ������ "Risks"

��������� ��������� ������ � ������� �� � ������������� ���������.

## ���������

1. ���������� ������ `pip3 install netbox-users-and-computers`
2. �������� ������ � `netbox/netbox/netbox/configuration.py` (�������� ��� �������� ����������):

```
PLUGINS=['users_and_computers']
```

3. ������� � ������� � ������ `manage.py` � ��������� �������� �� `python3 manage.py migrate`
4. ������������� ������ netbox
5. ���������, ��� ������ �������� � ������ ������������� �������� � ���������������� ���������� Django.

