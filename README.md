# finance complaint

for linux:
$(pwd)/airflow/dags

docker run -p 8080:8080 -v %cd%\airflow\dags:/app/airflow/dags finance:latest

```
echo "# finance-complaint" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/abhishek-jana/finance-complaint.git
git push -u origin main
```