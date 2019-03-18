.PHONY: test

test:
	PYTHONPATH=".:src/proto" pytest -v -s

gen_proto:
	python -m grpc_tools.protoc -I./proto --python_out=./src/proto --grpc_python_out=./src/proto ./proto/*.proto

run_web:
	PYTHONPATH=".:src/proto" python src/web/main.py

run_image_processing:
	PYTHONPATH=".:src/proto" python src/image_processing/main.py
