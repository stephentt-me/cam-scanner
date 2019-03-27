run-dev:
	PYTHONPATH=".:proto" python src/main.py

gen-proto:
	python -m grpc_tools.protoc -I./../protobuf-definition --python_out=./proto --grpc_python_out=./proto ../protobuf-definition/*.proto
