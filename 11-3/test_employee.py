from employee import Employee

def test_give_default_raise():
    emp = Employee('chloe', 'drakeford', 50000)
    emp.give_raise()
    assert emp.salary == 55000

def test_give_custom_raise():
    emp = Employee('chloe', 'drakeford', 50000)
    emp.give_raise(10000)
    assert emp.salary == 60000