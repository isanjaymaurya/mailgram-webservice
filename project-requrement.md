# Installation
1. https://redis.io/docs/install/install-redis/install-redis-on-windows/


# Project Requirement
0. Tech Stack - Django, MySQL, Jinja, Celary, Redies, Tailwind in Jinja
1. user can auth with jwt token
2. currently form can be in jinja. but in future we will use drf.
3. User can have mutiple contacts whome they can send email/newsletter
4. we will have no. of newsletters templates which user can select
5. user can create CRUD a campaigns.
6. in each compaign he can add users and select newletter which want to send and dynamic values can be provided
7. newletter templates are in jinja html, we will pass the dynamic context
8. all the newsletter will be go async on timing configured on their campaign ex 10 PM or 12 AM. with record for status for each day saved. we will use celary here.
9. if any newsletter failed to deliver we will have their records for failed same for success

# future
10. user can create their staff and staff will have access permission based like create/modify/delete contacts, modify newsletter, modify compains.
11. apis can be provided to perform all the operations
12. 