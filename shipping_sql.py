# ECHO is on.
import json
import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


app = FastAPI()
class Shipping_data(BaseModel):
    order_id: str
    customer_name: str
    region: str
    shipping_address: str
    weight_kg: float
    shipping_cost_usd: float
    status: str
    order_date: str
    delivery_date:str
# print(data)

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="7396656009",
    database="ShippingData"
)


f=open("C:\\Users\\ASHISH\\Documents\\shipping_data.json")
data=json.load(f) 
# print(data)

def insert_data_into_db():
    cursor=conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS shipping_data")
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS shipping_data (
                            order_id VARCHAR(10) PRIMARY KEY,
                            customer_name VARCHAR(100),
                            region VARCHAR(100),
                            shipping_address VARCHAR(150),
                            weight_kg FLOAT,
                            shipping_cost_usd FLOAT,
                            status VARCHAR(100),
                            order_date DATE,
                            delivery_date DATE
                        );
                        """)

    for record in data:
        cursor.execute("""INSERT INTO shipping_data
                            (order_id, customer_name, region, shipping_address, weight_kg, shipping_cost_usd, status, order_date, delivery_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, (
                                record["order_id"],
                                record["customer_name"],
                                record["region"],
                                record["shipping_address"],
                                record["weight_kg"],
                                record["shipping_cost_usd"],
                                record["status"],
                                record["order_date"],
                                record["delivery_date"]
                            ))
                    
        conn.commit()
        print("insterted successfully")

        cursor.execute("SELECT * FROM shipping_data")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    cursor.close()
    conn.close()
    return {'data inserted successfully'}


@app.get('/get-record/{order_id}')
def get_data(order_id):
    print(order_id)
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="7396656009",
    database="ShippingData"
)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM shipping_data WHERE order_id="{order_id}"')
    res = list(cursor)
    cursor.close()
    conn.close()

    return {'data': res}


@app.get('/get-customer-name/{region}')
def get_name(region):
    cursor=conn.cursor()
    cursor.execute(f'SELECT customer_name FROM shipping_data WHERE region ="{region}"')
    res=list(cursor)
    # cursor.commit()
    cursor.close()
    conn.close()
    return {'data':res}



@app.put('/put-order/{order_id}')
def insert_record(order_id,_shipping: Shipping_data):
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="7396656009",
    database="ShippingData"
)
    cursor=conn.cursor()
    query="""INSERT INTO shipping_data
                            (order_id, customer_name, region, shipping_address, weight_kg, shipping_cost_usd, status, order_date, delivery_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
    Values = ( 
            _shipping.order_id,
            _shipping.customer_name,
            _shipping.region,
            _shipping .shipping_address,
            _shipping.weight_kg,
            _shipping.shipping_cost_usd,
            _shipping.status,
            _shipping.order_date,
            # datetime.datetime.strptime(_shipping.order_date, '%Y-%m-%d'),
            # datetime.datetime.strptime(_shipping.delivery_date, '%Y-%m-%d')
            _shipping.delivery_date
                                )
    cursor.execute(query, Values)
    conn.commit()
    cursor.close()
    conn.close()
    return {'MEssage': 'success'}


@app.post('/get-update/{order_id}')
def update(order_id, update_db:Shipping_data):
    conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="7396656009",
                database="ShippingData")
    
    cursor=conn.cursor()
    
    query = """
        UPDATE Shipping_data
        SET 
            customer_name = %s,
            region = %s,
            shipping_address = %s,
            weight_kg = %s,
            shipping_cost_usd = %s,
            status = %s,
            order_date = %s,
            delivery_date = %s
        WHERE order_id = %s;
    """
    values = (
                update_db.order_id,
                update_db.customer_name,
                update_db.region,
                update_db.shipping_address,
                update_db.weight_kg,
                update_db.shipping_cost_usd,
                update_db.status,
                update_db.order_date,
                update_db.delivery_date
            )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Data Updated successfully"}


@app.delete("/delete_data/{order_id}")
def deleteData(order_id):
        conn=mysql.connector.connect(
         host="localhost",
        user="root",
        password="7396656009",
        database="ShippingData")

    
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM Shipping_data WHERE order_id = "{order_id}";')
        conn.commit()
        cursor.close()
        conn.close()

        return {"Message: Deleted Successfully"}

