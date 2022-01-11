```sql
select products.*,companies.name as company_name
from
products 
inner join companies ON products.company_id = companies.id;
```
