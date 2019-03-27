.PHONY: test

FLAG = PYTHONPATH=".:proto"

run:
	$(FLAG) gunicorn --bind 0.0.0.0:5000 --workers 8 --threads 8 --pythonpath src 'src.main:create_app()'

run-dev:
	$(FLAG) python src/main.py

test:
	$(FLAG) pytest .

gen-proto:
	python -m grpc_tools.protoc -I./../protobuf-definition --python_out=./proto --grpc_python_out=./proto ../protobuf-definition/*.proto

gen-doc:
	aglio -i documentation/apis/APIDoc.md -o dist-api-docs/index.html
