# skim-mind

An application which helps individuals improve their reading speed and efficiency using mindfulness meditation. This application provides an environment where users can focus on reading content without getting
distracted. Users can submit images and pdfs or just plain text they want to read.

## Tech Stack:

- **Backend:** Django/DRF
- **Frontend:** HTML/CSS/JavaScript
- **Hosted Link:** <a href="http://skimmind.herokuapp.com/">skim-mind</a>

## Features:

- Supports reading from plain text.
- Supports reading from pdf files.
- Supports reading from image files.

## API Endpoints:

```http
POST /api/text
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` | **Required**. Text to be processes |

```http
POST /api/pdf
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `pdf` | `file` | **Required**. Pdf File |

```http
POST /api/image
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `image` | `file` | **Required**. Image File in jpeg format |

## Response

```json
[
  { "word" : "word1", "factor" : "factor1" }
  { "word" : "word2", "factor" : "factor2" }
  { "word" : "word3", "factor" : "factor3" }
]
```

## Screenshots:

![skim-mind](https://user-images.githubusercontent.com/26035412/161446678-dc07e4b3-7965-45cd-b0a1-104cca7b29d2.png)

![skim-mind2](https://user-images.githubusercontent.com/26035412/161446691-5b9b7b45-9920-45d7-aa5e-154b45323caf.png)
