## Example message payload
```json
{
	"id": "0@dc6381da-0cab-46c0-8e08-dc7693028d6b",
	"disease": "mock-disease",
	"reference": {
		"bucket": "diagnostic-images-repository",
		"key": "public/dc6381da-0cab-46c0-8e08-dc7693028d6b/0.jpg"
	},
	"date": "2023-10-12T15:32:45.123456Z",
	"size": 1944,
	"diagnosis": "dc6381da-0cab-46c0-8e08-dc7693028d6b",
	"sample": 0
}
```

## Expected result
```json
{
	"mock.disease:mock": [
		{"x": 638, "y": 1218},
		{"x": 394, "y": 1109}
	]
}
```
