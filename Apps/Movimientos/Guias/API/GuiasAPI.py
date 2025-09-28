from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.Movimientos.Guias.API.SerializerGuias import GuiasSerializer
from Apps.Movimientos.Guias.models import Guia
from Apps.Utils.ResponseData import ResponseData


class GuiasViewSet(ModelViewSet):
    queryset = Guia.objects.select_related('IdReserva')
    serializer_class = GuiasSerializer

    def list(self, request):
        #Filtra solo guías activos
        filtro = Guia.objects.select_related('Reserva').all()
        serializer = GuiasSerializer(filtro, many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha listado correctamente",
            Record=serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk= int):
        try:
            serch = Guia.objects.get(pk=pk)
            serializer = GuiasSerializer(serch)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Guia.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el numero de cedula",
                Record=None
            )
            return Response(data, status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = GuiasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Cedu = Guia.objects.filter(cedula=serializer.validated_data['cedula']).exists()

        if Cedu:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="La cedula ya existe",
                Record=None
            )
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.toResponse())

        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a creado el nuevo registro",
            Record= serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk= int, **kwargs):
        partial = kwargs.get('partial', False)
        try:
            person = Guia.objects.get(pk=pk)
            serializer = GuiasSerializer(instance=person, data= request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="El registro se actualizo correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Guia.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha podido actualizar el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk= int):
        try:
            pos = Guia.objects.get(pk=pk)
            if not pos.is_Active:
                data = ResponseData(
                    Success=False,
                    Status=status.HTTP_404_NOT_FOUND,
                    Message="El registro esta desactivado",
                    Record=None
                )
                return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
            # Si esta Activo
            pos.is_Active = False
            pos.save()
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha Desactivado correctamente",
                Record=None
            )

            return Response(status=status.HTTP_200_OK, data=data.toResponse())
        except Guia.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea desactivar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())