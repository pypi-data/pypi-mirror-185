# History

## 0.1.16

Added

* Step options to SwitchGuideStepDependency to control Step state per Guide definition
* Extend SwitchGuideDefinitionOptions with availableOnMarketplaceForUserType to control whether the Guide is visible on the Marketplace
  * Options are None, All, or SwitchUserOnly

## 0.1.15

Added

* Switch Forms Extensions
  * Provides convenience methods for building and fetching form data
    * See method documentation for more information
    * Usage:
      * ```python
        import switch_api as sw
        import switch_guides as sg

        # Build UI Component
        sg.extensions.forms.define_ui_component(form_id=form_id)

        # Fetch Form Data
        form_data = sg.extensions.forms.get_data(api_inputs=api_inputs, form_id=form_id)
        section = form_data.getSectionById(1) # or form_data.getSectionByName('Section Name') 
        field = section.getFieldById(1) # or form_data.getFieldByLabel('Field Label')
        field_value = field.value
        ```

## 0.1.14

Updated

* Improved Guide Definition Registration Responses
  * Errors associated with registration will be available in the responses
* Documentation for most Guide types and properties

Added

* Aliases for guide.models modules so they are accessible on top level import
  * Few Examples:
    * ```python
      import switch_guides as sg

      sg.tasks.GuideStepDefinitionTask
      sg.step.SwitchGuideStepDefinition
      sg.guide.SwitchGuideDefinition
      sg.api.SwitchGuideStepProcessInput
      ```
* GuideStepDefinitionBackgroundTask that runs process() function in the background allowing users to navigate away from the page.
  * Will work in conjunction with LivelyUI APIs so that user can be given live feedback on the progress of the process method.
* More step control options:
  * uiState now has `continueToNextStep` and `continueToNextStepWhenAvailable` available
  * we can now set uiState on process response without requiring status property to be set
    * Example:
      ```python
      # Instead of:
      return SwitchGuideStepApiResponse(
          status=SwitchGuideStepStatus(
              uiState=SwitchGuideStepStatusUiState(
                  returnToSummary=True
              )
          )
      )

      # We can set uiState as:
      return SwitchGuideStepApiResponse(
          uiState=SwitchGuideStepStatusUiState(
              returnToSummary=True
          )
      )
      ```

## 0.1.13

Initial Switch Guides Release
