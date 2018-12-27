import traceback
import insufficient_funds
class Account:
  minbalance = 1000

  def __init__(self, name, acctype, balance):
    self.name = name
    self.acctype = acctype
    self.balance = balance

  def deposit(self, amt):
    self.balance += amt

  def withdrawl(self, amt):
    if self.balance - amt < Account.minbalance:
      raise insufficient_funds.InsufficientFundsError('Min balance of {0} not getting maintained'.format(Account.minbalance))
    self.balance -= amt
    return self.balance


if __name__ == '__main__':
  a1 = Account('mehul chopra', 'current', 5000)
  a1.deposit(3000)

  print(a1.balance) # -> 8000

  try:
    updated_bal = a1.withdrawl(8000)
  except insufficient_funds.InsufficientFundsError:
    traceback.print_exc()
  else:
    print('Withdrawl successful with updated bal {0}'.format(updated_bal))