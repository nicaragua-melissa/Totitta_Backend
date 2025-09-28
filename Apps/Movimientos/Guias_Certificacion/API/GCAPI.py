from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Apps.Movimientos.Guias_Certificacion.API.SerializerGC import GCSerializer
from Apps.Movimientos.Guias_Certificacion.models import Guia_Certificacion
from Apps.Utils.ResponseData import ResponseData


class GCViewSet(ModelViewSet):
    queryset = Guia_Certificacion.objects.select_related('Guia','certificacion')
    serializer_class = GCSerializer

    def list(self, request):
        queryset = Guia_Certificacion.objects.select_related('Guia','certificacion').all()
        serializer = GCSerializer(queryset, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha listado correctamente",
            Record=serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Guia_Certificacion.objects.get(pk=pk)
            serializer = GCSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a buscado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Guia_Certificacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = GCSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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
            loans = Guia_Certificacion.objects.get(pk=pk)
            serializer = GCSerializer(loans, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a actualizada correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Guia_Certificacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk: int):
        try:
            cert = Guia_Certificacion.objects.get(pk=pk)
            cert.delete()  # elimina físicamente el registro
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha eliminado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Guia_Certificacion.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea eliminar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
