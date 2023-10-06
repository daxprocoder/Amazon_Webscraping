const productContainer = document.getElementById('product-container');
const categoryLinks = document.querySelectorAll('.category-link');
const cartCounter = document.getElementById('cart-counter');

// Cart items object to store selected products and quantities
const cartItems = {};

// Event listener for category links
categoryLinks.forEach(link => {
    link.addEventListener('click', () => {
        const categoryId = link.id;
        fetch(`${categoryId}.json`)
            .then(response => response.json())
            .then(data => {
                // Clear existing products
                productContainer.innerHTML = '';

                // Loop through each product in the data
                data.data.forEach(product => {
                    const item = document.createElement('div');
                    item.classList.add('item');

                    const img = document.createElement('img');
                    img.src = product.main_img;
                    img.alt = product.title;

                    const h2 = document.createElement('h2');
                    h2.textContent = product.title;

                    const pPrice = document.createElement('p');
                    pPrice.textContent = `Price: ${product.price}`;

                    const addToCartButton = document.createElement('button');
                    addToCartButton.classList.add('add-to-cart-button');
                    addToCartButton.textContent = 'Add to Cart';

                    // Add click event to the Add to Cart button
                    addToCartButton.addEventListener('click', () => {
                        const productId = product.id; // Assign a unique ID to each product in JSON data
                        if (cartItems[productId]) {
                            cartItems[productId] += 1; // Increment quantity if product is already in cart
                        } else {
                            cartItems[productId] = 1; // Add product to cart with quantity 1
                        }
                        updateCartCounter(); // Update cart counter
                    });

                    // Append elements to item
                    item.appendChild(img);
                    item.appendChild(h2);
                    item.appendChild(pPrice);
                    item.appendChild(addToCartButton);

                    // Append item to product container
                    productContainer.appendChild(item);
                });
            })
            .catch(error => console.error('Error fetching products:', error));
    });
});

// Function to update cart counter
function updateCartCounter() {
    const totalItems = Object.values(cartItems).reduce((total, quantity) => total + quantity, 0);
    cartCounter.textContent = totalItems;
}



// Update cart counter on page load (in case some items are already in cart)
updateCartCounter();
