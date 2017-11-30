## Project Setup

You will need pip, git and python3 installed.

1. Clone the repo:

  ```sh
  $ git clone https://github.com/sugataa/word_count.git
  $ cd word_count
  ```

2. Create and activate your virtual env:

  ```sh
  $ python3 -m venv env
  $ source env/bin/activate
  ```

  > **NOTE**: You know that you are in a virtual env, as the actual "env" is now showing before the $ in your terminal - (env). To exit the virtual environment, use the command `deactivate`, then you can reactivate by navigating back to the directory and running - `source env/bin/activate`.

3. Install dependencies with pip:

  ```sh
  (env)$ pip install -r requirements.txt
  ```

4. Ensure tests are passing:

  ```sh
  (env)$ python app-test.py
  ```

5. Run the application:

  ```sh
  (env)$ python app.py
  ```

6. Navigate to http://localhost:5000
