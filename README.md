# Pet-Care

## How to install 
1. clone the project `clone [project url]`
2. make migration `>>py manage.py migrate`

## End-Points that need authentication
1. To access admin Panel >> `http://127.0.0.1:8000/admin`  `email:admin@gmail.com, password: adminn`
2. To delete User >> `http://127.0.0.1:8000/auth/employer/delete/<id>`
3. To Git Specific user >> `http://127.0.0.1:8000/auth/employer/<id>`
4. crud to Animal allow [POST,GET, PUT, DELETE]>> `http://127.0.0.1:8000/product/animal`
5. crud to Food allow [POST,GET, PUT, DELETE]>> `http://127.0.0.1:8000/product/food`
6.crud to Supplier allow[POST,GET, PUT, DELETE]>>  `http://127.0.0.1:8000/product/supllier`
7. To Logout >> `http://127.0.0.1:8000/auth/logout/`

## End-Points that don't need authentication
1. To login User >>`http://127.0.0.1:8000/auth/login/`
2. To Refresh access token >> `http://127.0.0.1:8000/auth/token/refresh/`
3. To Create User >> `http://127.0.0.1:8000/auth/employer/create/`
4. To Get all User >> `http://127.0.0.1:8000/auth/employer/list/`
