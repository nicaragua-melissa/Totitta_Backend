from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.Movimientos.Reservacion.API.SerializerReservacion import ReservacionSerializer
from Apps.Movimientos.Reservacion.models import Reservacion
from Apps.Utils.ResponseData import ResponseData


class ReservacionViewSet(ModelViewSet):
    queryset = Reservacion.objects.select_related('Reserva')
    serializer_class = ReservacionSerializer

    def list(self, request):
        queryset = Reservacion.objects.select_related('Reserva').all()
        serializer = ReservacionSerializer(queryset, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha listado correctamente",
            Record=serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Reservacion.objects.get(pk=pk)
            serializer = ReservacionSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a buscado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Reservacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = ReservacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = Reservacion.objects.filter(code=serializer.validated_data['Codigo_Reserva']).exists()
        if code:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="Ya existe esa reservacion",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message="Se a creado el registro",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk=int):
        try:
            loans = Reservacion.objects.get(pk=pk)
            serializer = ReservacionSerializer(loans, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a actualizada correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Reservacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk: int):
        try:
            cert = Reservacion.objects.get(pk=pk)
            cert.delete()  # elimina físicamente el registro
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha eliminado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Reservacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea eliminar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
