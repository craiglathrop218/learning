from wfconfig import WorkfrontConfig
from application.controllers.wf_controllers.wf_project_controller import WFProjectController

p = WFProjectController(api_key=WorkfrontConfig.api_key,
                        subdomain=WorkfrontConfig.subdomain,
                        env=WorkfrontConfig.env)

p.load_project('59ab1b0200b48d92cfaefb590aa32fc4')

