from copy import deepcopy

import pytest

import src.app as app_module


_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    monkeypatch.setattr(app_module, "activities", deepcopy(_INITIAL_ACTIVITIES))
