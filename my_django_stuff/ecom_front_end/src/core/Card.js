import React from "react";
// import imageHelper from "./helper/imageHelper";
import ImageHelper from "./helper/imageHelper";
import Redirect from "react-router-dom";

const isAuthenticated = false;
const removeFromcart = true;
const Card = ({ product }) => {
  const cartTitle = product ? product.name : "A photo from pexel";
  const cartDescription = product ? product.description : "Default Description";
  const cartPrice = product ? product.price : "500";

  const addTocart = () => {
    if (isAuthenticated) {
      console.log("Added to Cart!");
    } else {
      console.log("Login Please!");
    }
  };

  const showaddTocart = (addTocart) => {
    return (
      addTocart && (
        <button
          onClick={addTocart}
          className="btn btn-block btn-outline-success mt-2 mb-2"
        >
          Add to Cart
        </button>
      )
    );
  };

  const showremoveFromcart = (removeFromcart) => {
    return (
      removeFromcart && (
        <button
          onClick={() => {
            console.log("Product Removed SuccessFully!");
          }}
          className="btn btn-block btn-outline-danger mt-2 mb-2"
        >
          Remove from cart
        </button>
      )
    );
  };
  return (
    <div className="card text-white bg-dark border border-info ">
      <div className="card-header lead">{cartTitle}</div>
      <div className="card-body">
        <ImageHelper product={product} />
        <p className="lead bg-success font-weight-normal text-wrap">
          {cartDescription}
        </p>
        <p className="btn btn-success rounded  btn-sm px-4">Rs. {cartPrice}</p>
        <div className="row">
          <div className="col-12">{showaddTocart(addTocart)}</div>
          <div className="col-12">{showremoveFromcart(removeFromcart)}</div>
        </div>
      </div>
    </div>
  );
};

export default Card;
