# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:24:45 2019

@author: macl3

URL: https://www.codewars.com/kata/sql-basics-top-10-customers-by-total-payments-amount/train/sql
"""

SELECT customer.customer_id, customer.email, count(payment.payment_id) as payments_count, cast (sum(payment.amount) as float) as total_amount
FROM customer, payment
where customer.customer_id = payment.customer_id
group by customer.customer_id
order by total_amount desc
limit 10