from wfconfig import WorkfrontConfig
from application.controllers.wf_controllers.wf_project_controller import WFProjectController

p = WFProjectController(api_key=WorkfrontConfig.api_key,
                        subdomain=WorkfrontConfig.subdomain,
                        env=WorkfrontConfig.env)

