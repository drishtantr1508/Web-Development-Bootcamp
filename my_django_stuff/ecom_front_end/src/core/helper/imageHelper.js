import React from "react";

export default function ImageHelper({ product }) {
  const imageurl = product
    ? product.image
    : `https://images.pexels.com/photos/1566412/pexels-photo-1566412.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500`;
  return (
    <div className="rounded border border-success p-2">
      <img
        src={imageurl}
        alt=""
        style={{ maxHeight: "100%", maxWidth: "100%" }}
        className="mb-3 rounded"
      />
    </div>
  );
}
