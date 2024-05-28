## JavaScript SDK example usage
## Installation

Include the ExperimentSDK script in the `<head>` of your website:

```html
<script src="cdn/wwai.js"></script>
```

## Example Usage

```
(async function () {
    const experimentId = 1;
    const variantAssignment = await ExperimentSDK.determineVariantForUser(experimentId);
    console.log('User assigned to variant:', variantAssignment.assignment.variant_id);
})();

```

## Endpoints

### User Endpoints

#### Create a User

- **URL:** `/users`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "hashed_id": "unique_hashed_id",
        "attributes": {
            "device_type": "mobile",
            "location": "US"
        }
    }
    ```
- **Response:**
    ```json
    {
        "message": "User created successfully",
        "user": {
            "id": 1,
            "hashed_id": "unique_hashed_id",
            "attributes": {
                "device_type": "mobile",
                "location": "US"
            }
        }
    }
    ```

#### Get a User

- **URL:** `/users/<hashed_id>`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "id": 1,
        "hashed_id": "unique_hashed_id",
        "attributes": {
            "device_type": "mobile",
            "location": "US"
        }
    }
    ```

### Experiment Endpoints

#### Create an Experiment

- **URL:** `/experiments`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "Experiment 1",
        "description": "Description of experiment 1",
        "start_date": "2024-01-01 00:00:00",
        "end_date": "2024-12-31 23:59:59",
        "status": "active"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Experiment created successfully",
        "experiment": {
            "id": 1,
            "name": "Experiment 1",
            "description": "Description of experiment 1",
            "start_date": "2024-01-01 00:00:00",
            "end_date": "2024-12-31 23:59:59",
            "status": "active"
        }
    }
    ```

#### Get All Experiments

- **URL:** `/experiments`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Experiment 1",
            "description": "Description of experiment 1",
            "start_date": "2024-01-01 00:00:00",
            "end_date": "2024-12-31 23:59:59",
            "status": "active"
        }
    ]
    ```

### Variant Endpoints

#### Create a Variant

- **URL:** `/variants`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "experiment_id": 1,
        "name": "Variant A",
        "description": "Description of variant A",
        "weight": 0.5
    }
    ```
- **Response:**
    ```json
    {
        "message": "Variant created successfully",
        "variant": {
            "id": 1,
            "experiment_id": 1,
            "name": "Variant A",
            "description": "Description of variant A",
            "weight": 0.5
        }
    }
    ```

#### Get Variants by Experiment

- **URL:** `/variants/<experiment_id>`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Variant A",
            "description": "Description of variant A",
            "weight": 0.5
        }
    ]
    ```

#### Update Variant Weights

- **URL:** `/variants/weights`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "experiment_id": 1,
        "weights": {
            "1": 0.3,
            "2": 0.7
        }
    }
    ```
- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Variant A",
            "description": "Description of variant A",
            "weight": 0.3
        },
        {
            "id": 2,
            "name": "Variant B",
            "description": "Description of variant B",
            "weight": 0.7
        }
    ]
    ```

### User Assignment Endpoints

#### Assign User to Variant

- **URL:** `/assign`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "hashed_id": "unique_hashed_id",
        "experiment_id": 1,
        "attributes": {
            "device_type": "mobile",
            "location": "US"
        }
    }
    ```
- **Response:**
    ```json
    {
        "message": "User assigned to variant successfully",
        "assignment": {
            "user_id": 1,
            "experiment_id": 1,
            "variant_id": 1,
            "timestamp": "2024-05-28T12:34:56.789Z"
        }
    }
    ```