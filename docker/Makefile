# Variables
DOCKER_REPOSITORY=yyzhang4/open-webui
IMAGE_TAG=0.1.5.3

# Build Docker images
build:
	@echo "Building web Docker image: $(DOCKER_REPOSITORY):$(IMAGE_TAG)..."
	docker-compose build
	@echo "Web Docker image built successfully: $(DOCKER_REPOSITORY):$(IMAGE_TAG)"

# Push Docker images
push:
	@echo "Pushing web Docker image: $(DOCKER_REPOSITORY):$(IMAGE_TAG)..."
	docker push $(DOCKER_REPOSITORY):$(IMAGE_TAG)
	@echo "Web Docker image pushed successfully: $(DOCKER_REPOSITORY):$(IMAGE_TAG)"

release: build push