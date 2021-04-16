test: ## Run test
	docker build -t nginxproxy/nginx-proxy:test .
	./test/requirements/build.sh
	./test/pytest.sh

.DEFAULT_GOAL := help

# kudos to: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY : help test
help :
	@grep -E '^[a-zA-Z_-]+ *:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = " *:.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
