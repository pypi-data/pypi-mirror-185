
DeliveryForm = function (params) {

    var $deliveryMethod = params.$deliveryMethod,
        $city = params.$city,
        $warehouse = params.$warehouse,
        deliveryMethods = params.deliveryMethods,
        citiesUrl = params.citiesUrl,
        warehousesUrl = params.warehousesUrl,
        $warehouseLabel = $('[data-role=warehouse-label]'),
        $addressLabel = $('[data-role=address-label]'),
        $deliveryTypes = $('[data-role=novaposhta-delivery-types]'),
        $selfDeliveryOption = $('[data-role=novaposhtaselfdelivery]');

    setEvents();
    handleDeliveryMethodChange();
    updateAddressLabel();

    function setEvents() {
        $deliveryMethod.on('change', handleDeliveryMethodChange);
        $city.on('change', handleCityChange);
        $('[name=novaposhtatype]').change(updateAddressLabel);
    }

    function handleDeliveryMethodChange() {

        var method = $deliveryMethod.val(),
            action = (
                !method || method == deliveryMethods.self_delivery
            ) ? 'hide' : 'show';

        $city.parent()[action]();
        $warehouse.parent()[action]();
        $deliveryTypes[action]();

        $city.autocomplete({
            serviceUrl: citiesUrl,
            width: 'auto',
            minChars: 2,
            onSelect: function () {
                $(this).trigger('change');
            }
        });

        $warehouse.autocomplete({
            serviceUrl: warehousesUrl,
            width: 'auto',
            minChars: 1,
            params: getWarehouseParams()
        });

    }

    function handleCityChange() {
        $warehouse.val('');
        $warehouse.autocomplete('setOptions', {params: getWarehouseParams()});
    }

    function updateAddressLabel() {
        if ($selfDeliveryOption.is(':checked')) {
            $warehouseLabel.show();
            $addressLabel.hide();
        } else {
            $warehouseLabel.hide();
            $addressLabel.show();
        }
    }

    function getWarehouseParams() {
        return {
            delivery_method: $deliveryMethod.val(),
            city: $city.val()
        };
    }

};
