from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from .forms import BookingForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'admin_dashboard/login.html')

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bookings')
    else:
        form = BookingForm()
    return render(request, 'admin_dashboard/booking_form.html', {'form': form})

@login_required
def list_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'admin_dashboard/booking_list.html', {'bookings': bookings})

@login_required
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('list_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'admin_dashboard/booking_form.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('list_bookings')
    return render(request, 'admin_dashboard/booking_confirm_delete.html', {'booking': booking})

@login_required
def cancel_booking(request):
    if request.method == 'POST':
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            try:
                # Find the booking to cancel
                booking = Booking.objects.get(name=name, phone=phone, is_canceled=False)
                # Mark the booking as canceled
                booking.is_canceled = True
                booking.save()

                messages.success(request, f"Booking for {name} on {booking.date} at {booking.time} has been canceled.")
                return redirect('list_bookings')
            except Booking.DoesNotExist:
                form.add_error(None, "No active booking found with the provided details.")
    else:
        form = CancelBookingForm()

    return render(request, 'admin_dashboard/cancel_booking.html', {'form': form})