# $NetBSD$

DISTNAME=	grpcio_status-1.76.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/grpcio_status/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://grpc.io
COMMENT=	Status proto mapping for gRPC
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-googleapis-common-protos>=1.5.5:../../devel/py-googleapis-common-protos
DEPENDS+=	${PYPKGPREFIX}-grpcio>=1.76.0:../../net/py-grpcio
DEPENDS+=	${PYPKGPREFIX}-coverage>=4.0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-cython>=3.1.1:../../devel/py-cython
DEPENDS+=	${PYPKGPREFIX}-protobuf>=6.31.1:../../devel/py-protobuf
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=4.12.2:../../devel/py-typing-extensions

USE_LANGUAGES=	# none

#BUILDLINK_API_DEPENDS.protobuf+=	protobuf>=6.31.1,<7.0.0

.include "../../devel/protobuf/buildlink3.mk"
.include "../../devel/py-cython/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
