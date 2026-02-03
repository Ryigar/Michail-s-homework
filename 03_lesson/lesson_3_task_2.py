from smartphone import Smartphone
phone1 = Smartphone('Samsung', 's23', '+79623334455')
phone2 = Smartphone('LG', 'F999', '+75603401098')
phone3 = Smartphone('Huawei', 'g100', '+74569992121')
phone4 = Smartphone('Xiaomi', 'Mi999', '+78886667700')
phone5 = Smartphone('Poco', 'X6Pro', '+70009522233')

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.mark} - {phone.model}. {phone.number}")
