from datetime import timedelta
from dateutil.parser import parse
import pytest
from freezegun import freeze_time


@pytest.mark.django_db
def test_is_active(phase):
    module = phase.module
    with freeze_time(phase.start_date):
        assert module.is_active
    with freeze_time(phase.end_date):
        assert not module.is_active


@pytest.mark.django_db
def test_is_active_in_project(phase_factory, module, module_factory):
    phase = phase_factory(
        module=module,
        start_date=parse('2013-01-01 00:00:00 UTC'),
        end_date=parse('2013-01-10 00:00:00 UTC')
    )
    module2 = module_factory(project=module.project)
    phase2 = phase_factory(
        module=module2,
        start_date=parse('2013-01-05 00:00:00 UTC'),
        end_date=parse('2013-01-15 00:00:00 UTC')
    )
    with freeze_time(phase.start_date - timedelta(minutes=1)):
        assert not module.is_active_in_project
        assert not module2.is_active_in_project
    with freeze_time(phase.start_date):
        assert module.is_active_in_project
        assert not module2.is_active_in_project
    with freeze_time(phase2.start_date):
        assert module.is_active_in_project
        assert not module2.is_active_in_project
    with freeze_time(phase2.end_date - timedelta(minutes=1)):
        assert not module.is_active_in_project
        assert module2.is_active_in_project
    with freeze_time(phase2.end_date):
        assert not module.is_active_in_project
        assert not module2.is_active_in_project


@pytest.mark.django_db
def test_active_phase(phase):
    module = phase.module
    with freeze_time(phase.start_date):
        assert module.active_phase == phase
    with freeze_time(phase.start_date - timedelta(days=1)):
        assert module.active_phase is None


@pytest.mark.django_db
def test_first_phase_start_date(phase, phase_factory):
    module = phase.module
    first_phase = phase_factory(
        module=module, start_date=phase.start_date - timedelta(days=1))
    assert module.first_phase_start_date == first_phase.start_date


@pytest.mark.django_db
def test_phases(phase, phase_factory):
    module = phase.module
    phase2 = phase_factory(module=module)
    assert list(module.phases) == [phase, phase2]


@pytest.mark.django_db
def test_future_phases(phase, phase_factory):
    module = phase.module
    phase_factory(
        module=module,
        start_date=phase.start_date - timedelta(days=3),
        end_date=phase.start_date - timedelta(days=2))
    with freeze_time(phase.start_date - timedelta(days=1)):
        assert list(module.future_phases) == [phase]


@pytest.mark.django_db
def test_past_phases(phase, phase_factory):
    module = phase.module
    phase_factory(
        module=module,
        start_date=phase.end_date + timedelta(days=2),
        end_date=phase.end_date + timedelta(days=3))
    with freeze_time(phase.end_date + timedelta(days=1)):
        assert list(module.past_phases) == [phase]


@pytest.mark.django_db
def test_last_active_phase(phase, phase_factory):
    module = phase.module
    last_active_phase = phase_factory(
        module=module,
        start_date=phase.end_date + timedelta(days=2),
        end_date=phase.end_date + timedelta(days=3))
    with freeze_time(last_active_phase.end_date + timedelta(days=1)):
        assert module.last_active_phase == last_active_phase
