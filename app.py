from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {
        "name": "Laptop",
        "price": "$500",
        "image": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8"
    },
    {
        "name": "Headphones",
        "price": "$80",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    },
    {
        "name": "Smart Watch",
        "price": "$120",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        "name": "Mobile Phone",
        "price": "$300",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    }
]

HTML = """

<!DOCTYPE html>
<html>
<head>
    <title>E-Commerce Website</title>

    <style>

        body{
            margin:0;
            font-family: Arial;
            background:#f4f4f4;
        }

        nav{
            background:#111;
            padding:15px;
            text-align:center;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin:20px;
            font-size:18px;
        }

        .hero{
            height:300px;
            background:linear-gradient(to right,#4facfe,#00f2fe);
            color:white;
            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction:column;
            animation: fade 2s;
        }

        @keyframes fade{
            from{opacity:0;}
            to{opacity:1;}
        }

        .products{
            display:flex;
            flex-wrap:wrap;
            justify-content:center;
            padding:20px;
        }

        .card{
            background:white;
            width:250px;
            margin:15px;
            border-radius:15px;
            overflow:hidden;
            box-shadow:0 0 10px gray;
            transition:0.4s;
        }

        .card:hover{
            transform:scale(1.05);
        }

        .card img{
            width:100%;
            height:200px;
            object-fit:cover;
        }

        .card h2, .card p{
            text-align:center;
        }

        button{
            display:block;
            margin:15px auto;
            padding:10px 20px;
            border:none;
            background:#007BFF;
            color:white;
            border-radius:8px;
            cursor:pointer;
        }

        .about{
            padding:40px;
            text-align:center;
            background:white;
        }

        .pagination{
            text-align:center;
            padding:20px;
        }

        .pagination button{
            margin:10px;
        }

        footer{
            background:#111;
            color:white;
            text-align:center;
            padding:20px;
        }

    </style>

</head>

<body>

    <nav>
        <a href="#">Home</a>
        <a href="#products">Products</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>

    <div class="hero">
        <h1>Welcome To My E-Commerce Website</h1>
        <p>Buy Amazing Products Online</p>
    </div>

    <section id="products" class="products">

        {% for product in products %}

        <div class="card">
            <img src="{{ product.image }}">
            <h2>{{ product.name }}</h2>
            <p>{{ product.price }}</p>
            <button>Buy Now</button>
        </div>

        {% endfor %}

    </section>

    <div class="pagination">
        <button>⬅ Previous Page</button>
        <button>Next Page ➡</button>
    </div>

    <section id="about" class="about">
        <h1>About Us</h1>
        <p>
            We create professional E-Commerce websites with animation,
            product gallery, buttons, pages and modern design using Python Flask.
        </p>
    </section>

    <footer id="contact">
        <h2>Contact Us</h2>
        <p>Email: ecommerce@gmail.com</p>
    </footer>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML, products=products)

if __name__ == "__main__":
    app.run(debug=True)