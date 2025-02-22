import pytest
import auth.auth_data as auth_data

from castoredc_api_study.castor_study import CastorStudy


@pytest.fixture(scope="class")
def integration_study():
    study = CastorStudy(
        auth_data.client_id,
        auth_data.client_secret,
        auth_data.test_client_study_id,
        "data.castoredc.com",
    )
    return study
