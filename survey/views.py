from django.shortcuts import render
from .forms import GeneralInformationForm, BusinessTypeForm, BusinessFieldForm, BusinessSizeForm, StrategyOperationForm, GeneralFeedbackForm

def survey_view(request):
    if request.method == "POST":
        # Create form instances with POST data
        general_form = GeneralInformationForm(request.POST)
        business_type_form = BusinessTypeForm(request.POST)
        business_field_form = BusinessFieldForm(request.POST)
        business_size_form = BusinessSizeForm(request.POST)
        strategy_form = StrategyOperationForm(request.POST)
        feedback_form = GeneralFeedbackForm(request.POST)
        
        # Check if all forms are valid
        if all([general_form.is_valid(), business_type_form.is_valid(), business_field_form.is_valid(), business_size_form.is_valid(), strategy_form.is_valid(), feedback_form.is_valid()]):
            # Save all forms to the database
            general_form.save()
            business_type_form.save()
            business_field_form.save()
            business_size_form.save()
            strategy_form.save()
            feedback_form.save()

            # Render the "Thank You" page after saving the data
            return render(request, "survey/thank_you.html")
    else:
        # Initialize empty forms for GET request
        general_form = GeneralInformationForm()
        business_type_form = BusinessTypeForm()
        business_field_form = BusinessFieldForm()
        business_size_form = BusinessSizeForm()
        strategy_form = StrategyOperationForm()
        feedback_form = GeneralFeedbackForm()
    
    # Render the form template with all forms passed in the context
    return render(request, "survey/survey_form.html", {
        "general_form": general_form,
        "business_type_form": business_type_form,
        "business_field_form": business_field_form,
        "business_size_form": business_size_form,
        "strategy_form": strategy_form,
        "feedback_form": feedback_form,
    })

def thank_you_view(request):
    # Render the Thank You page after successful form submission
    return render(request, 'survey/thank_you.html')
