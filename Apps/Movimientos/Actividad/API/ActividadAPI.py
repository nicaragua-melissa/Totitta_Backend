from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.Movimientos.Actividad.API.SerializerActividad import ActividadSerializer
from Apps.Movimientos.Actividad.models import Actividad
from Apps.Utils.ResponseData import ResponseData


class ActividadViewSet(ModelViewSet):
    queryset = Actividad.objects.select_related('Reserva')
    serializer_class = ActividadSerializer

    def list(self, request):
        queryset = Actividad.objects.select_related('Reserva').all()
        serializer = ActividadSerializer(queryset, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha listado correctamente",
            Record=serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Actividad.objects.get(pk=pk)
            serializer = ActividadSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a buscado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Actividad.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = ActividadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Even = Actividad.objects.filter(CodigoActividad=serializer.validated_data['CodigoActividad']).exists()
        if Even:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="Ya existe esa Actividad",
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

    def update(self, request, pk=int, **kwargs):
        partial = kwargs.get('partial', False)
        try:
            loans = Actividad.objects.get(pk=pk)
            serializer = ActividadSerializer(loans, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a actualizada correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Actividad.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk: int):
        try:
            cert = Actividad.objects.get(pk=pk)
            cert.delete()  # elimina físicamente el registro
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha eliminado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Actividad.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea eliminar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
