install:
		uv sync

brain-games:
		uv run brain-games

build:
		uv build

package-install:
		uv tool install dist/*.whl

reinstall-package:
		uv tool install --upgrade dist/*.whl
