from model.contact import Contact


def test_add_new_contact(app):
  app.session.login(username="admin", password="secret")
  app.contact.create(Contact(firstname="test1", middlename="test1", lastname="test1", nickname="test1", title="test1", company="test1", address="test1", home="test1", mobile="test1", work="test1", fax="test1", email="test1", email2="test1", email3="test1", homepage="test1", address2="test1", phone2="test1", notes="test1",bday="14",bmonth="June"))
  app.session.logout()


def test_add_empty_contact(app):
  app.session.login(username="admin", password="secret")
  app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", address2="", phone2="", notes="",bday="",bmonth=""))
  app.session.logout()



  
