import React, { useState, useEffect } from "react";
import { getProducts } from "./helper/coreapicalls";
import Base from "./Base";
import Card from "./Card";
import styles from "../styles.css";
// import Card from "./Card";
function Home() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(false);

  const loadAllProducts = () => {
    getProducts().then((data) => {
      if (data.error) {
        setError(data.error);
        console.log(data.error);
      } else {
        setProducts(data);
      }
    });
  };

  useEffect(() => {
    loadAllProducts();
  }, []);

  return (
    <Base title="Welcome to Drishtant's T-shirt Store">
      <h1>Home Component</h1>
      <div className="row">
        {products.map((product, index) => {
          return (
            <div key={index} className="col-4 mb-4">
              <Card product={product} />
            </div>
          );
        })}

        {/* <Card />
        <Card /> */}
        {/* <Card /> */}
      </div>
    </Base>
  );
}
export default Home;
