import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../Style/productlist.scss";

function ProductList() {
  // State variables for products, search term, filtered products, and error message
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [error, setError] = useState("");

  // Fetch products from the backend API
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/products", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });
        setProducts(response.data);
        setFilteredProducts(response.data);
      } catch (error) {
        setError("Failed to fetch products");
      }
    };

    fetchProducts();
  }, []);

  // Filter products based on search term
  const handleSearch = () => {
    const filtered = products.filter(
      (product) =>
        product.name.toLowerCase().includes(search.toLowerCase()) ||
        product.category.toLowerCase().includes(search.toLowerCase())
    );
    setFilteredProducts(filtered);
  };

  return (
    <div className="product-list-container">
      <h2>Product Catalog</h2>
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search by name or category"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      {error && <p>{error}</p>}
      <ul>
        {filteredProducts.map((product) => (
          <li key={product.id}>
            <Link to={`/products/${product.id}`}>
              <h3>{product.name}</h3>
            </Link>
            <p>Category: {product.category}</p>
            <p>Record Count: {product.record_count}</p>
            <p>Fields: {product.fields}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
