document.addEventListener("DOMContentLoaded", function () {
    const ingredientsSection = document.getElementById('ingredientsSection');
    const addIngredientButton = document.getElementById('addIngredient');
    const recipeForm = document.getElementById('recipeForm');
    const resultsDiv = document.getElementById('results');

    // Function to add a new ingredient input
    addIngredientButton.addEventListener('click', function () {
        const newIngredientDiv = document.createElement('div');
        newIngredientDiv.classList.add('ingredientInput');

        const newIngredientInput = document.createElement('input');
        newIngredientInput.type = 'text';
        newIngredientInput.name = 'ingredient';
        newIngredientInput.placeholder = 'Ingredient';
        newIngredientInput.required = true;

        const removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.classList.add('removeIngredient');
        removeButton.textContent = 'Remove';

        newIngredientDiv.appendChild(newIngredientInput);
        newIngredientDiv.appendChild(removeButton);
        ingredientsSection.appendChild(newIngredientDiv);

        removeButton.addEventListener('click', function () {
            ingredientsSection.removeChild(newIngredientDiv);
        });
    });

    // Handle form submission
    recipeForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const ingredients = Array.from(document.querySelectorAll('input[name="ingredient"]')).map(input => input.value);
        const dietary = document.getElementById('dietary').value;
        const cuisine = document.getElementById('cuisine').value;

        // Display search results (dummy implementation)
        resultsDiv.innerHTML = `<h2>Search Results</h2>
                                <p>Ingredients: ${ingredients.join(', ')}</p>
                                <p>Dietary Restriction: ${dietary}</p>
                                <p>Cuisine Type: ${cuisine}</p>`;
    });
});
