# Security policy for `.env` files and GitHub Actions

## Working with `.env` files locally

1. All required `.env` keys are stored inside the `.env.example` of each working directory
2. Take all the keys and fill them with the values
3. Please be careful not to accidentally commit a `.env` file, even though it's in `.gitignore`.
4. When you add a new key to the `.env` file, please also update the `.env.example`.