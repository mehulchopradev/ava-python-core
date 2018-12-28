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
    print('Transaction starts...')

    try:
      if amt <= 0:
        raise ValueError('Amt to withdraw must be a positive non zero value')
      if self.balance - amt < Account.minbalance:
        raise insufficient_funds.InsufficientFundsError('Min balance of {0} not getting maintained'.format(Account.minbalance))
      self.balance -= amt
      return self.balance
    finally:
      # come what may in the corresponding try block ,this block with its statements will always execute
      print('Transaction ends.')


if __name__ == '__main__':
  a1 = Account('mehul chopra', 'current', 5000)
  a1.deposit(3000)

  print(a1.balance) # -> 8000

  try:
    updated_bal = a1.withdrawl(9000)
  except insufficient_funds.InsufficientFundsError:
    traceback.print_exc()
  except ValueError:
    traceback.print_exc()
  else:
    print('Withdrawl successful with updated bal {0}'.format(updated_bal))