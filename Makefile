install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl

