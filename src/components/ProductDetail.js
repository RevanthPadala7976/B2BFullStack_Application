import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../Style/productdetails.scss"; // Import component-specific SCSS

function ProductDetail() {
  const { id } = useParams(); // Get product ID from URL parameters
  const [product, setProduct] = useState(null); // State variable for product details
  const [error, setError] = useState(""); // state varibale for error message

  // Fetch product details from the backend API
  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/products/${id}`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
          }
        );
        setProduct(response.data);
      } catch (error) {
        setError("Failed to fetch product details");
      }
    };

    fetchProduct();
  }, [id]);

  if (error) {
    return <p>{error}</p>;
  }

  if (!product) {
    return <p>Loading...</p>;
  }

  return (
    <div className="product-detail-container">
      <h2>{product.name}</h2>
      <p>Category: {product.category}</p>
      <p>Record Count: {product.record_count}</p>
      <p>Fields: {product.fields}</p>
    </div>
  );
}

export default ProductDetail;
